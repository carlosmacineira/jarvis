import { motion } from 'framer-motion'
import { clsx } from 'clsx'
import { twMerge } from 'tailwind-merge'

export default function GlassCard({ children, className, animate = true, ...props }) {
  const Component = animate ? motion.div : 'div'
  const animateProps = animate
    ? {
        initial: { opacity: 0, y: 20 },
        animate: { opacity: 1, y: 0 },
        transition: { duration: 0.6, ease: [0.22, 1, 0.36, 1] },
      }
    : {}

  return (
    <Component
      className={twMerge(
        clsx(
          'rounded-2xl border border-glass-border',
          'bg-white/[0.04] backdrop-blur-2xl',
          'shadow-[0_8px_32px_rgba(0,0,0,0.4)]',
          className
        )
      )}
      {...animateProps}
      {...props}
    >
      {children}
    </Component>
  )
}
