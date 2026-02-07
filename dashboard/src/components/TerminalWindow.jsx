import { useState, useEffect } from 'react'
import { motion } from 'framer-motion'
import GlassCard from './GlassCard'

const bootSequence = [
  { text: '> Initializing Jarvis Core v3.2.1 ...', delay: 0 },
  { text: '> Loading neural mesh network ...', delay: 600 },
  { text: '> Establishing secure uplink ... OK', delay: 1200 },
  { text: '> Cognitive engine: ONLINE', delay: 1900 },
  { text: '> Memory banks: 64 TB allocated', delay: 2400 },
  { text: '> System diagnostics: ALL GREEN', delay: 3000 },
  { text: '> Voice synthesis: calibrated', delay: 3500 },
  { text: '> Spatial awareness: active', delay: 4000 },
  { text: '> Ready. Awaiting command, sir.', delay: 4800 },
]

export default function TerminalWindow() {
  const [lines, setLines] = useState([])

  useEffect(() => {
    const timers = bootSequence.map(({ text, delay }) =>
      setTimeout(() => setLines((prev) => [...prev, text]), delay)
    )
    return () => timers.forEach(clearTimeout)
  }, [])

  return (
    <GlassCard className="w-[380px] overflow-hidden">
      {/* Title bar */}
      <div className="flex items-center gap-2 px-4 py-3 border-b border-glass-border">
        <div className="flex gap-1.5">
          <div className="w-2.5 h-2.5 rounded-full bg-accent-rose/70" />
          <div className="w-2.5 h-2.5 rounded-full bg-yellow-500/70" />
          <div className="w-2.5 h-2.5 rounded-full bg-accent-emerald/70" />
        </div>
        <span className="ml-2 text-xs tracking-widest uppercase text-glass-muted">
          Terminal
        </span>
      </div>

      {/* Terminal body */}
      <div className="p-4 h-64 overflow-y-auto font-mono text-[13px] leading-relaxed">
        {lines.map((line, i) => (
          <motion.div
            key={i}
            initial={{ opacity: 0, x: -8 }}
            animate={{ opacity: 1, x: 0 }}
            transition={{ duration: 0.3 }}
            className={
              line.includes('Ready')
                ? 'text-accent-emerald'
                : line.includes('OK') || line.includes('ONLINE') || line.includes('GREEN')
                  ? 'text-orb-glow'
                  : 'text-glass-muted'
            }
          >
            {line}
          </motion.div>
        ))}
        {/* Blinking cursor */}
        <motion.span
          className="inline-block w-2 h-4 bg-orb-glow/80 ml-0.5 align-middle"
          animate={{ opacity: [1, 0, 1] }}
          transition={{ duration: 1.1, repeat: Infinity }}
        />
      </div>
    </GlassCard>
  )
}
