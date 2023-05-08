// Add the following JavaScript code

// Get the form elements
const topicInput = document.getElementById('topic');
const gradeInput = document.getElementById('grade');
const boardInput = document.getElementById('board');
const getStartedButton = document.querySelector('.button');

// Add an event listener to the "Get Started" button
getStartedButton.addEventListener('click', () => {
  const topic = topicInput.value;
  const grade = gradeInput.value;
  const board = boardInput.value;
  
  // Perform some action with the entered values
  console.log('Topic:', topic);
  console.log('Grade:', grade);
  console.log('Board:', board);
});
