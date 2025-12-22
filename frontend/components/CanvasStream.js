'use client'

import { useRef, useEffect } from "react";

export default function CanvasStream({ wsUrl }) {
  const canvasRef = useRef(null);
  const frameRef = useRef(null);

  useEffect(() => {
    const ws = new WebSocket(wsUrl);
    ws.binaryType = "arraybuffer";
    ws.onmessage = (event) => {
      console.log("Frame received", event.data);
      frameRef.current = event.data;
    };
    let running = true;
    function draw() {
      if (frameRef.current && canvasRef.current) {
        const ctx = canvasRef.current.getContext("2d");
        const img = new window.Image();
        img.onload = () => ctx.drawImage(img, 0, 0);
        img.src = URL.createObjectURL(new Blob([frameRef.current]));
        frameRef.current = null;
      }
      if (running) requestAnimationFrame(draw);
    }
    draw();
    return () => { running = false; ws.close(); };
  }, [wsUrl]);

  return <canvas ref={canvasRef} width={800} height={600} />;
}