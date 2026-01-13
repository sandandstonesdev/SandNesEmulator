.segment "HEADER"
  .byte 'N', 'E', 'S', $1A ; $4E, $45, $53, $1A Format Magic
  .byte 2                  ; 2x 16KB PRG
  .byte 1                  ; 1x  8KB CHR
  .byte $01, $00           ; Mapper 0, Vertical Mirroring
  .byte $00
  .byte $00, $00, $00, $00, $00, $00, $00 ; Padding

.segment "CHRDATA"
  .incbin "alphabet.chr"
  .incbin "alphabet.chr"

.segment "VECTORS"
  .word nmi
  .word reset
  .word 0 ; IRQ vector unused

.segment "ZEROPAGE"
  spr_base_x : .res 1
  spr_base_y : .res 1

.segment "CODE"
reset:
  sei
  cld
  ldx #$40
  stx $4017
  ldx #$ff
  txs
  inx
  stx $2000 
  stx $2001
  stx $4010

; wait for first vblank
vblankwait1:
  bit $2002
  bpl vblankwait1

; clear RAM
clear_memory:
  lda #$00
  sta $0000, x
  sta $0100, x
  sta $0200, x
  sta $0300, x
  sta $0400, x
  sta $0500, x
  sta $0600, x
  sta $0700, x
  inx
  bne clear_memory

; wait for second vblank
vblankwait2:
  bit $2002
  bpl vblankwait2

main:
  ; Load palettes
  lda $2002
  lda #$3f
  sta $2006
  lda #$00
  sta $2006
  ldx #$00
@pal_loop:
  lda palettes, x
  sta $2007
  inx
  cpx #$20
  bne @pal_loop

; Init variables
  lda #$40
  sta spr_base_x
  lda #$70
  sta spr_base_y

; Prepare sprite OAM buffer for message
  ldx #$00           ; X = message index (0..0x14)
  ldy #$00           ; Y = OAM buffer index (increments by 4)

sprite_init:
  lda message, x
  sta $0201, y ; tile index
  lda #$02      ; attributes (palette 2) const
  sta $0202, y
  
  lda spr_base_x        ; base X position
  sta $0203, y
  txa
  asl
  asl
  asl
  clc
  adc $0203, y    ; x position offset
  cmp #$80
  beq adjust
  sta $0203, y    ; x position
  jmp not_adjust
adjust: ; if x = 80 => base_x = 0; base_y += 16
  sec
  lda spr_base_x
  sbc #$40
  sta spr_base_x
  clc
  lda spr_base_y
  adc #$10
  sta spr_base_y
  cmp #$90
  bne not_adjust
  sec
  sbc #$50
  sta $0203, y    ; x position
not_adjust:
  lda spr_base_y          ; Y position const
  sta $0200, y
  inx
  iny
  iny
  iny
  iny
  cpx #$14
  bne sprite_init

enable_rendering:
  lda #%10001000 ; SPR ; BG 1
  sta $2000
  lda #%00010000
  sta $2001
game_loop:
  jmp game_loop

nmi:
  ; Transfer OAM buffer to PPU OAM
  ldx #$00
  stx $2003
  lda #$02
  sta $4014
  rti

.segment "PRGDATA"
; 2109 - 2148 Offsets
message:
 ; ASCII: "SANDNES EMULATOR"
 .byte $33, $21, $2E, $24, $2E, $25, $33, $20, $25, $2D, $35, $2C, $21, $34, $2F, $32
 .byte $12, $10, $12, $16 ; 2026 
palettes:
  ; BG (blue background, light blue highlight)
  .byte $0F, $12, $22, $32
  .byte $0F, $12, $22, $32
  .byte $0F, $12, $22, $32
  .byte $0F, $12, $22, $32
  ; SPR (green for visible letters)
  .byte $0F, $19, $29, $39
  .byte $0F, $19, $29, $39
  .byte $0F, $19, $29, $39
  .byte $0F, $19, $29, $39
