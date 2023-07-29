#!/usr/bin/node

const fetch = require('node-fetch');

function computeCompletedTasks(apiUrl) {
  fetch(apiUrl)
    .then((response) => {
      if (!response.ok) {
        throw new Error(`HTTP error! Status: ${response.status}`);
      }
      return response.json();
    })
    .then((data) => {
      const userCompletedTasks = {};

      data.forEach((task) => {
        if (task.completed) {
          const userId = task.userId;
          userCompletedTasks[userId] = (userCompletedTasks[userId] || 0) + 1;
        }
      });

      for (const userId in userCompletedTasks) {
        console.log(`User ID ${userId}: ${userCompletedTasks[userId]} completed tasks`);
      }
    })
    .catch((error) => {
      console.error('Error:', error);
    });
}

const apiUrl = 'https://jsonplaceholder.typicode.com/todos';
computeCompletedTasks(apiUrl);
