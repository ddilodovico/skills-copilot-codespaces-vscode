// Create Web server
// 1. Create a Web server
// 2. Read the comments from the comments.json file
// 3. Display the comments on the Web server

// 1. Create a Web server
// Import the http module
const http = require('http');
// Import the fs module
const fs = require('fs');
// Import the url module
const url = require('url');

// Create a Web server
const server = http.createServer((req, res) => {
    // 2. Read the comments from the comments.json file
    fs.readFile('./comments.json', 'utf-8', (err, data) => {
        if (err) {
            res.writeHead(404, { 'Content-Type': 'text/plain' });
            res.end('File not found');
        } else {
            const comments = JSON.parse(data);

            // 3. Display the comments on the Web server
            res.writeHead(200, { 'Content-Type': 'application/json' });
            res.end(JSON.stringify(comments));
        }
    });
});

// Listen for incoming requests
server.listen(3000, '