import React from 'react'
import Navbar from '../components/layout/Navbar'
import Footer from '../components/layout/Footer'
import FileCard from '../components/FileCard'
import FileUpload from '../components/upload/FileUpload'

export default function Home() {
  return (
    <div className='min-h-screen bg-slate-50 flex flex-col'>
      <Navbar/>

      <div className='max-w-5xl mx-auto w-full px-4 sm:px-6 pt-6 sm:pt-10'>
        <FileCard/>
      </div>

      <main className='max-w-5xl mx-auto w-full px-4 sm:px-6 py-8 sm:py-10 flex-1'>
        <FileUpload/>
      </main>

      <Footer/>
    </div>
  )
}