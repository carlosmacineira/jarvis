import { motion } from 'framer-motion'
import Orb from './components/Orb'
import Dock from './components/Dock'
import TerminalWindow from './components/TerminalWindow'
import SystemVitals from './components/SystemVitals'

export default function App() {
  return (
    <div className="relative w-full h-screen overflow-hidden">
      {/* Mesh gradient background */}
      <div className="mesh-bg" />

      {/* Main spatial layout */}
      <div className="relative z-10 flex items-center justify-center w-full h-full">
        {/* Left panel — Terminal */}
        <motion.div
          className="absolute left-8 top-1/2 -translate-y-1/2 animate-float"
          initial={{ opacity: 0, x: -60 }}
          animate={{ opacity: 1, x: 0 }}
          transition={{ duration: 0.9, delay: 0.2, ease: [0.22, 1, 0.36, 1] }}
          style={{ animationDelay: '0.5s' }}
        >
          <TerminalWindow />
        </motion.div>

        {/* Center — Orb */}
        <motion.div
          initial={{ opacity: 0, scale: 0.6 }}
          animate={{ opacity: 1, scale: 1 }}
          transition={{ duration: 1, ease: [0.22, 1, 0.36, 1] }}
        >
          <Orb />
        </motion.div>

        {/* Right panel — System Vitals */}
        <motion.div
          className="absolute right-8 top-1/2 -translate-y-1/2 animate-float"
          initial={{ opacity: 0, x: 60 }}
          animate={{ opacity: 1, x: 0 }}
          transition={{ duration: 0.9, delay: 0.4, ease: [0.22, 1, 0.36, 1] }}
          style={{ animationDelay: '1.5s' }}
        >
          <SystemVitals />
        </motion.div>
      </div>

      {/* Bottom dock */}
      <Dock />

      {/* Top status bar */}
      <motion.div
        className="fixed top-0 left-0 right-0 z-50 flex items-center justify-between px-8 py-4"
        initial={{ opacity: 0, y: -20 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ duration: 0.8, delay: 0.8 }}
      >
        <span className="text-xs tracking-[0.3em] uppercase text-glass-muted font-light">
          Jarvis Dashboard
        </span>
        <div className="flex items-center gap-3">
          <div className="w-1.5 h-1.5 rounded-full bg-accent-emerald animate-pulse" />
          <span className="text-xs tracking-wider text-glass-muted">
            All Systems Nominal
          </span>
        </div>
      </motion.div>
    </div>
  )
}
