import React from 'react'

export default function ErrorMessage({message, onClose}) {
  if(!message) return null

  return (
    <div  className="mt-4 flex items-center justify-between rounded-lg border border-red-300 bg-red-50 px-4 py-3 text-red-700"
          role="alert">
          <div className='flex items-center gap-2'>
             <span>  </span>
             <p>{message}</p>
          </div>

          <button onClick={onClose}  className="mt-4 flex items-center justify-between rounded-lg border border-red-300 bg-red-50 px-4 py-3 text-red-700"
          role="alert"> ✕</button>
    </div>
  )
}
