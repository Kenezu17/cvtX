import React from 'react'
import logo from '../../assets/images/logo.jpg';

function Navbar() {
  return (
    <nav className='sticky top-0 z-50 bg-white/80 backdrop-blur-md border-b border-slate-200/80'>
  <div className='max-w-7xl mx-auto h-16 px-4 sm:px-6 flex justify-center items-center'>
    <div className='flex items-center gap-2'>
      <img src={logo} className='w-8 h-8 object-contain' alt="ConvertX logo" />
      <h1 className='text-xl font-bold tracking-tight text-slate-900'>
        Convert<span className='text-blue-600'>X</span>
      </h1>
    </div>

  </div>
</nav>
  )
}

export default Navbar