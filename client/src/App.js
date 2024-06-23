import React, { useState } from 'react';
import Header from './components/Header';
import ResumeInput from './components/ResumeInput';
import TextInput from './components/TextInput';
import Toggle from './components/Toggle';

function App() {
  const [resume, setResume] = useState(null);
  const [bio, setBio] = useState("");
  const [result, setResult] = useState(null);

  const handleResumeChange = (e) => {
    const file = e.target.files[0];
    setResume(file);
  };

  const handleBioChange = (e) => {
    setBio(e.target.value);
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    const formData = new FormData();
    formData.append('resume', resume);
    formData.append('bio', bio);
    console.log(formData.get('resume'));
    console.log(formData.get('bio'));

    try {
      const response = await fetch('http://127.0.0.1:5000/api/submit', { // Replace with your endpoint URL
        method: 'POST',
        body: formData,
        mode: 'cors',
      });

      if (!response.ok) {
        console.log(response);
        throw new Error('Network response was not ok');
      }

      const result = await response.json();
      setResult(result);
      console.log('Success:', result);
    } catch (error) {
      console.error('Error:', error);
    }
  };

  const renderValues = (data) => {
    if (typeof data === 'object') {
      if (Array.isArray(data)) {
        return data.map((item, index) => (
          <div key={index} className="mt-2">
            {renderValues(item)}
          </div>
        ));
      } else {
        return Object.values(data).map((value, index) => (
          <div key={index} className="mt-2">
            {renderValues(value)}
          </div>
        ));
      }
    }
    return <div>{data}</div>;
  };

  return (
    <div className="flex flex-col md:flex-row">
      <div className="h-full w-full flex flex-col mx-auto items-center space-y-8 justify-center">
        <Header />
        <form onSubmit={handleSubmit} className="space-y-12 items-center flex flex-col w-full">
          <ResumeInput onChange={handleResumeChange} />
          <TextInput onChange={handleBioChange} />
          <Toggle />
          <button type="submit" className="btn btn-primary">Submit</button>
        </form>
      </div>
      <div className="w-4/5  md:w-1/3 border border-neutral m-4 rounded-md p-4 bg-gray-400 overflow-y-auto text-clip">
        <h1 className="text-base-100 border-b border-base-100 pb-2 text-xl">
          Results
        </h1>
        {result && (
          <div className="text-base-100 mt-4">
            {renderValues(result)}
          </div>
        )}
      </div>
    </div>
  );
}

export default App;





