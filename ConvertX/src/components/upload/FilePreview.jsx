import React from 'react'
import { FormatSizeFile } from '../../utils/formatSize'

function FilePreview({file, onRemove}) {
  return (
    <div className='mt-8 bg-slate-100 rounded-xl p-4 sm:p-5 '>
      <div className='min-w-0 flex-1'>
        <div>
           <h2 className='font-semibold text-gray-900 text-sm sm:text-base break-all pr-2'>
            {file.name}
        </h2>
        <p className='text-xs sm:text-sm text-gray-500 mt-0.5'>
             {FormatSizeFile(file.size)}
        </p>
        </div>

            <button
            onClick={onRemove}
            className='ursor-pointer px-2 py-2.5 sm:px-4 sm:py-2 text-xs sm:text-sm font-medium text-red-600 hover:text-red-700 hover:bg-red-50 rounded-lg focus:underline transition-colors shrink-0'
            > remove </button>

      </div>
    </div>
  )
}

export default FilePreview