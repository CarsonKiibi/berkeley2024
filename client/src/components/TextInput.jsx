import React from 'react';

function TextInput({ onChange }) {
    return (
        <textarea
            className="textarea textarea-bordered w-3/5 h-96 md:h-36 bg-gray-400 text-gray-900"
            placeholder="Enter your job description here!"
            onChange={onChange}
        ></textarea>
    );
}

export default TextInput;
