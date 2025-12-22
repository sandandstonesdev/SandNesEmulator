import CanvasStream from '../components/CanvasStream';

export default function Home() {
  return (
    <main className="flex min-h-screen flex-col items-center justify-center bg-gray-50">
      <h1>Python Stream Canvas</h1>
      <CanvasStream wsUrl="ws://localhost:8000/ws" />
    </main>
  );
}