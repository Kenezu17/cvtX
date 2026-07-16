import { useState } from "react";
import FilePreview from "./FilePreview";
import ConvertBtn from "../converter/ConvertBtn";
import ConvertOptionBtn from "../converter/ConvertOptionBtn";
import ProgressBar from "./ProgressBar";
import DownloadBtn from "../converter/DownloadBtn";

export default function FileUpload() {
  const [file, setFile] = useState(null);

  return (
    <div className="bg-white rounded-3xl shadow-lg p-10">

      <label
        className="border-2 border-dashed border-blue-400 rounded-2xl h-72 flex flex-col justify-center items-center cursor-pointer"
      >
        <input
          type="file"
          hidden
          onChange={(e) => setFile(e.target.files[0])}
        />

        <h2 className="text-2xl font-semibold">
          Click to Upload
        </h2>

        <p className="text-gray-500">
          or Drag & Drop
        </p>
      </label>

      {file && (
        <>
          <FilePreview file={file} />

          <ConvertOptionBtn />

          <ConvertBtn />

          <ProgressBar progress={0} />

          <DownloadBtn />
        </>
      )}

    </div>
  );
}