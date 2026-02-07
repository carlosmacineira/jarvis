import { motion } from 'framer-motion'
import { Terminal, Cpu, Home, Settings } from 'lucide-react'

const items = [
  { icon: Home, label: 'Home' },
  { icon: Terminal, label: 'Terminal' },
  { icon: Cpu, label: 'Vitals' },
  { icon: Settings, label: 'Settings' },
]

function DockItem({ icon: Icon, label }) {
  return (
    <motion.button
      className="group relative flex flex-col items-center gap-1"
      whileHover={{ scale: 1.2, y: -6 }}
      whileTap={{ scale: 0.95 }}
      transition={{ type: 'spring', stiffness: 400, damping: 17 }}
    >
      <div className="w-12 h-12 rounded-xl bg-white/[0.06] border border-glass-border backdrop-blur-xl flex items-center justify-center transition-colors group-hover:bg-white/[0.12] group-hover:border-glass-highlight">
        <Icon size={20} className="text-glass-muted group-hover:text-white transition-colors" />
      </div>
      <span className="text-[10px] tracking-wider uppercase text-glass-muted opacity-0 group-hover:opacity-100 transition-opacity">
        {label}
      </span>
    </motion.button>
  )
}

export default function Dock() {
  return (
    <motion.div
      className="fixed bottom-6 left-1/2 z-50"
      initial={{ opacity: 0, y: 40, x: '-50%' }}
      animate={{ opacity: 1, y: 0, x: '-50%' }}
      transition={{ duration: 0.8, delay: 0.6, ease: [0.22, 1, 0.36, 1] }}
    >
      <div className="flex items-end gap-3 px-5 py-3 rounded-2xl bg-white/[0.04] border border-glass-border backdrop-blur-2xl shadow-[0_8px_32px_rgba(0,0,0,0.5)]">
        {items.map((item) => (
          <DockItem key={item.label} {...item} />
        ))}
      </div>
    </motion.div>
  )
}
