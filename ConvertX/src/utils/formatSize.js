export function FormatSizeFile(bytes) {
    if (!bytes || bytes === 0) return '0 Bytes';


    const unit = ['Bytes', 'KB', 'MB', 'GB'];
    

    let index = Math.floor(Math.log(bytes) / Math.log(1024));

  
    if (index >= unit.length) index = unit.length - 1;

    
    const calculation = bytes / Math.pow(1024, index);
    
    return `${calculation.toFixed(2)} ${unit[index]}`;
}
