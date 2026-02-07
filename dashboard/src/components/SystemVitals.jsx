import { useState, useEffect } from 'react'
import { motion } from 'framer-motion'
import GlassCard from './GlassCard'

function CircularGauge({ label, value, color, maxVal = 100 }) {
  const radius = 36
  const circumference = 2 * Math.PI * radius
  const progress = (value / maxVal) * circumference
  const offset = circumference - progress

  return (
    <div className="flex flex-col items-center gap-2">
      <div className="relative w-24 h-24">
        <svg className="w-full h-full -rotate-90" viewBox="0 0 96 96">
          <circle
            cx="48" cy="48" r={radius}
            fill="none"
            stroke="rgba(255,255,255,0.06)"
            strokeWidth="5"
          />
          <motion.circle
            cx="48" cy="48" r={radius}
            fill="none"
            stroke={color}
            strokeWidth="5"
            strokeLinecap="round"
            strokeDasharray={circumference}
            initial={{ strokeDashoffset: circumference }}
            animate={{ strokeDashoffset: offset }}
            transition={{ duration: 1.5, ease: 'easeOut' }}
          />
        </svg>
        <div className="absolute inset-0 flex items-center justify-center">
          <span className="text-lg font-light text-glass-text">{value}%</span>
        </div>
      </div>
      <span className="text-[10px] tracking-[0.2em] uppercase text-glass-muted">{label}</span>
    </div>
  )
}

export default function SystemVitals() {
  const [cpu, setCpu] = useState(0)
  const [mem, setMem] = useState(0)

  useEffect(() => {
    // Simulate fluctuating metrics
    const simulate = () => {
      setCpu(Math.floor(Math.random() * 30) + 15)
      setMem(Math.floor(Math.random() * 20) + 42)
    }
    simulate()
    const interval = setInterval(simulate, 3000)
    return () => clearInterval(interval)
  }, [])

  return (
    <GlassCard className="px-6 py-5">
      <div className="flex items-center gap-2 mb-4">
        <div className="w-1.5 h-1.5 rounded-full bg-accent-emerald animate-pulse" />
        <span className="text-xs tracking-[0.2em] uppercase text-glass-muted">System Vitals</span>
      </div>
      <div className="flex gap-6">
        <CircularGauge label="CPU" value={cpu} color="#6366f1" />
        <CircularGauge label="Memory" value={mem} color="#3b82f6" />
      </div>
    </GlassCard>
  )
}
