import { useState, useRef } from "react";

import APIURL from "../../services/api";
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
  const [downloadFilename, setDownloadFilename] = useState('')
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

    try {
      const formData = new FormData();
      formData.append('file', file);
      formData.append('convert_to', toFormat);

      const response = await APIURL.post('/convert/', formData, {
        headers: { 'Content-Type': 'multipart/form-data' }
      });

      setProgress(100);
      setError('');
      setDownloadFilename(response.data.converted_filename);
      setIsDownloading(false);
    } catch (err) {
      setError(err?.response?.data?.detail || 'Conversion failed');
    } finally {
      setLoading(false);
    }
  }

const handleDonwload = async()=>{
   if(!downloadFilename) {
      setError('Convert the file first before downloading')
      return
   }

   setIsDownloading(true)
   setError('')

   const res = await DownlaodFile(downloadFilename)

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