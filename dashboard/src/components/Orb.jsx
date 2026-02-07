import { motion } from 'framer-motion'

export default function Orb() {
  return (
    <div className="relative flex items-center justify-center">
      {/* Outer glow rings */}
      <motion.div
        className="absolute w-72 h-72 rounded-full"
        style={{
          background: 'radial-gradient(circle, rgba(99,102,241,0.15) 0%, transparent 70%)',
        }}
        animate={{ scale: [1, 1.15, 1], opacity: [0.4, 0.7, 0.4] }}
        transition={{ duration: 5, repeat: Infinity, ease: 'easeInOut' }}
      />

      <motion.div
        className="absolute w-56 h-56 rounded-full"
        style={{
          background: 'radial-gradient(circle, rgba(99,102,241,0.1) 0%, transparent 70%)',
        }}
        animate={{ scale: [1.1, 1, 1.1], opacity: [0.3, 0.6, 0.3] }}
        transition={{ duration: 4, repeat: Infinity, ease: 'easeInOut', delay: 0.5 }}
      />

      {/* Core orb */}
      <motion.div
        className="relative w-32 h-32 rounded-full"
        style={{
          background: 'radial-gradient(circle at 35% 35%, #818cf8, #6366f1 50%, #4338ca 100%)',
          boxShadow: '0 0 60px rgba(99,102,241,0.5), 0 0 120px rgba(99,102,241,0.2), inset 0 0 30px rgba(255,255,255,0.1)',
        }}
        animate={{ scale: [1, 1.06, 1] }}
        transition={{ duration: 5, repeat: Infinity, ease: 'easeInOut' }}
      >
        {/* Specular highlight */}
        <div
          className="absolute top-3 left-5 w-12 h-8 rounded-full opacity-30"
          style={{
            background: 'radial-gradient(ellipse, rgba(255,255,255,0.6) 0%, transparent 70%)',
          }}
        />
      </motion.div>

      {/* Label */}
      <motion.p
        className="absolute -bottom-12 text-xs tracking-[0.3em] uppercase text-glass-muted"
        animate={{ opacity: [0.4, 0.8, 0.4] }}
        transition={{ duration: 4, repeat: Infinity, ease: 'easeInOut' }}
      >
        Jarvis Online
      </motion.p>
    </div>
  )
}
