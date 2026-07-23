import React from 'react'

function Footer() {
  return (
   
    <footer className='fixed bottom-0 left-0 right-0 w-full border-t border-slate-200 bg-white py-8'>
      <div className='max-w-7xl mx-auto px-4 sm:px-6 flex flex-col sm:flex-row items-center justify-center sm:justify-between gap-2 text-center sm:text-left text-xs sm:text-sm text-slate-500'>
        <p>© 2026 ConvertX. All Rights Reserved.</p>
        <p>
          Built by{' '}
          <a href="https://personal-website-kenezu17s-projects.vercel.app/"
            target='_blank'
            rel='noopener noreferrer'
            className='font-medium text-slate-700 hover:text-blue-600 underline underline-offset-2 transition-colors'>
            Kenezu Fumar
          </a>
        </p>
      </div>
    </footer>
  )
}

export default Footer
