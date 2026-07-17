import React from 'react'
import { DownlaodFile } from '../../utils/DownloadFile'
import { useState } from 'react'
function DownloadBtn({loading, onDowload}) {
  const[errDonwload, serErrDownload] = useState('')

  return (
    <div>
    <button
    onClick={onDowload}
    disabled={loading}
    className="mt-8 w-full bg-emerald-500 text-white py-4 rounded-xl hover:bg-emerald-600">
     {loading ?(
      <span className='flex items-center gap-2'>
        <svg className='animate-spin h-4 w-4 text-gray-400" viewBox="0 0 24 24'>
          <circle className='opacity-25" cx="12" cy="12" r="10" stroke="currentColor" strokeWidth="4" fill="none'/>
          <path className='opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4z'/>
        </svg>
        Downloading...
      </span>

     ):(
      'Download File'
     )}
    </button>
     {errDonwload && (
      <p className='text-shadow-red-500 text-sm mt-1 font-medium'role='alert'>
        {errDonwload}
      </p>
  
     )}
    </div>
  )
}

export default DownloadBtn