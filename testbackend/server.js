const express = require('express');
const cors = require('cors');
const app = express();
const port = 5000;

// Enable CORS for all routes
app.use(cors());
app.use(express.json());

app.post('/api/submit', (req, res) => {
    const { resume, jobDesc } = req.body;
    console.log('Resume:', resume);
    console.log('Bio:', jobDesc);
    res.json({ message: 'Data received successfully', resume, jobDesc });
});

app.listen(port, () => {
    console.log(`Server running on port ${port}`);
});