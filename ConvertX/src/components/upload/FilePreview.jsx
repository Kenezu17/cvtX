import React from 'react'

function FilePreview({file}) {
  return (
    <div className='mt-8 bg-slate-100 rounded-xl p-5'>
        <h2 className='font-semibold'>
            {file.name}
        </h2>
        <p className='text-gray-500'>
             {(file.zie / 1024 /1024 .toFixed(2))}mb
        </p>
    </div>
  )
}

export default FilePreview