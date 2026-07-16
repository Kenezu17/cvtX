import React, { use } from 'react'
import { useState } from 'react'
import covertFile from '../services/api'
function useFileUpload() {
  const[loading, setLoading] = useState(false)
  const[downloadUrl, setDownloadUrl] = useState('')

  const covert  = async(file) =>{
    setLoading(true)
    setDownloadUrl('')

    const formData = new FormData()
    formData.append('file', file)

    try {
      const data = await covertFile(formData)
      setDownloadUrl(data.download_url)
      
    } catch (err) {
      console.log(err)
    }
    finally{
      setLoading(false)
    }


  }
  return {
    loading,
   downloadUrl,
   covert
  }
   
}

export default useFileUpload