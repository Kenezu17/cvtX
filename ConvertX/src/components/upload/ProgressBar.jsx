import React from 'react'

function ProgressBar({ progress = 0 }) {
  const clamped = Math.max(0, Math.min(100, Number(progress) || 0))

  return (
    <div className='mt-8'>
      <div className='w-full h-3 bg-gray-200 rounded-full overflow-hidden'>
        <div
          role="progressbar"
          aria-label="Upload progress"
          aria-valuemin={0}
          aria-valuemax={100}
          aria-valuenow={clamped}
          style={{ width: `${clamped}%` }}
          className='bg-gradient-to-r from-blue-600 to-emerald-500 h-3 rounded-full transition-all duration-300 ease-linear'
        />
      </div>
      <p className='mt-2'>{clamped}%</p>
    </div>
  )
}

export default ProgressBar