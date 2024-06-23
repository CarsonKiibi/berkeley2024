import React from 'react';

function ResumeInput({ onChange }) {
    return (
        <div className="flex flex-col items-center space-y-2">
        <label className="label">Upload your resume</label>
        <input
            type="file"
            className="file-input file-input-bordered max-w-xs"
            accept="application/pdf"
            onChange={onChange}
        />
        </div>
    );
}

export default ResumeInput;
