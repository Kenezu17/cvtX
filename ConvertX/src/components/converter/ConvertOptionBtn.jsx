import React from 'react'

const options = [
  { label: 'PDF', value: 'pdf' },
  { label: 'DOCX', value: 'docx' },
  { label: 'JPG', value: 'jpg' },
  { label: 'PNG', value: 'png' },
  { label: 'Excel', value: 'xlsx' },
  { label: 'CSV', value: 'csv' },
]

function ConvertOptionBtn({ fromFormat, toFormat, onOptionChange }) {
  return (
    <div className='flex flex-col sm:flex-row items-center gap-3 sm:gap-4'>
      <select
        value={fromFormat}
        onChange={(e) => onOptionChange('from', e.target.value)}
        className='w-full border border-slate-300 rounded-lg p-3 text-slate-700 bg-white focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent'
      >
        {options.map((option) => (
          <option key={option.value} value={option.value}>
            {option.label}
          </option>
        ))}
      </select>

      <span className='text-slate-400 font-medium shrink-0'>to</span>

      <select
        value={toFormat}
        onChange={(e) => onOptionChange('to', e.target.value)}
        className='w-full border border-slate-300 rounded-lg p-3 text-slate-700 bg-white focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent'
      >
        {options.map((option) => (
          <option key={option.value} value={option.value}>
            {option.label}
          </option>
        ))}
      </select>
    </div>
  )
}

export default ConvertOptionBtn