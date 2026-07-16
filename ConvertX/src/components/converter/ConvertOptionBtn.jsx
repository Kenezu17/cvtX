import React from 'react'

function ConvertOptionBtn() {
  return (
    <div className='flex flex-col sm:flex-row items-center gap-3 sm:gap-4'>
    <select className='w-full border border-slate-300 rounded-lg p-3 text-slate-700 bg-white focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent'>
        <option>PDF</option>
        <option>DOCX</option>
        <option>JPG</option>
        <option>PNG</option>
        <option>Excel</option>
        <option>CSV</option>
    </select>

    <span className='text-slate-400 font-medium shrink-0'>to</span>

    <select className='w-full border border-slate-300 rounded-lg p-3 text-slate-700 bg-white focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent'>
        <option>DOCX</option>
        <option>PDF</option>
        <option>PNG</option>
        <option>JPG</option>
        <option>CSV</option>
        <option>Excel</option>
    </select>
  </div>
  )
}

export default ConvertOptionBtn