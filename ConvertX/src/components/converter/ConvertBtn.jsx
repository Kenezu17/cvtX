import React from 'react'


export default function ConvertBtn({loading, onClick}) {

  return (
   
      <button 
       onClick={onClick}
       disabled={loading}
      className="mt-8 w-full rounded-xl bg-linear-to-r from-blue-600 to-emerald-500 py-4 text-lg font-semibold text-white transition hover:opacity-90 disabled:cursor-not-allowed disabled:opacity-50">
      {loading ? "Converting...": "Convert File"}
    </button>

  )
}
