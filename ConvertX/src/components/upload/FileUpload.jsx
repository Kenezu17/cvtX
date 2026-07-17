import { useState,useRef } from "react";

import { validateSize, validateType } from "../../utils/fileValidation";
import { FILE_TYPES } from "../../utils/fileTypes";
import { DownlaodFile } from "../../utils/DownloadFile";

import FilePreview from "./FilePreview";
import ConvertBtn from "../converter/ConvertBtn";
import ConvertOptionBtn from "../converter/ConvertOptionBtn";
import ProgressBar from "./ProgressBar";
import DownloadBtn from "../converter/DownloadBtn";
import ErrorMessage from "../ErrorMessage";

export default function FileUpload() {
  const [file, setFile] = useState(null);
  const [error, setError] = useState('')
  const [loading, setLoading] = useState(false)
  const inputRef = useRef(null)
  const [progress, setProgress] = useState(0)
  const [isDownloading, setIsDownloading] = useState(false)
  const [fromFormat, setFromFormat] = useState('pdf')
  const [toFormat, setToFormat] = useState('docx')

  const removeFile = () => {
    setFile(null)
  }

  const handlefilechange = (e) => {
    const selectFile = e.target.files[0]

    if (!selectFile) return

    setFile(selectFile)
    setError('')
  }

  const handleOptionChange = (type, value) => {
    if (type === 'from') {
      setFromFormat(value)
    } else {
      setToFormat(value)
    }
  }

  const handleConvert = async () => {
    if (!file) {
      setError('Please select a file')
      return
    }

    const size = validateSize(file)

    if (!size.valid) {
      setError(size.message)
      return
    }

    const formatMap = {
      pdf: 'pdf',
      docx: 'word',
      jpg: 'image',
      png: 'image',
      excel: 'excel',
      csv: 'csv',
    }

    const selectedType = FILE_TYPES[formatMap[fromFormat]] || []
    const type = validateType(file, selectedType)

    if (!type.valid) {
      setError(type.message)
      return
    }

    setError('')
    setLoading(true)
  }

const handleDonwload = async()=>{
   if(!isDownloading) return

   setIsDownloading(true)
   setError('')

   const res = await DownlaodFile(file)

   if(!res.success){
      setError(res.message)
   }

   setIsDownloading(false)

}

  return (
    <div className="bg-white rounded-3xl shadow-lg p-10">

      <label
        className="border-2 border-dashed border-blue-400 rounded-2xl h-72 flex flex-col justify-center items-center cursor-pointer"
      >
        <input
          type="file"
          hidden
          onChange={handlefilechange}
        />

        <h2 className="text-2xl font-semibold">
          Click to Upload
        </h2>

        <p className="text-gray-500">
          or Drag & Drop
        </p>
      </label>

      <ErrorMessage
      message={error}
      onClose={()=> setError('')}
      />

      {file && (
        <>
          <FilePreview 
          onRemove={removeFile}
          file={file} />

          <ConvertOptionBtn
            fromFormat={fromFormat}
            toFormat={toFormat}
            onOptionChange={handleOptionChange}
          />

          <ConvertBtn 
            loading={loading}
            onClick={handleConvert}
          />

          <ProgressBar progress={progress} />

          <DownloadBtn
            loading={isDownloading}
            onDowload={handleDonwload}
          />
        </>
      )}

    </div>
  );
}