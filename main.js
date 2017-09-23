var problemList = [
  {
    name: 'Ulohasassssssss c.1',
    hash: '688787d8ff144c502c7f5cffaafe2cc588d86079f9de88304c26b0cb99ce91c6',
    correct: 'c9022680f888674e2b2274758755bfa07dea729b68d71cde5c521ed70ef261bf',
  },
  {
    name: 'Uloha c.2',
    hash: 'cc00113f2c36b6d0e501dd832771ce5db7b41c1d77edb22b5fde8baf1c5e449b',
    correct: '259aa8ef98a8b91de574cd904138ef643240c23080cf24da4793a6f10a43fa9d',
  },
]

function getElem(id) {
  return document.getElementById(id)
}

function createNameKey(name) {
  return name.replace(/\s+/g, '').toLowerCase();
}

// create options for select
var selectElem = getElem('problem-select')
for (var i = 0; i < problemList.length; i++) {
  var opt = document.createElement('option');
  opt.text = problemList[i].name;
  opt.value = problemList[i].name;

  selectElem.add(opt, null);
}

var submitElem = getElem('submit')
var textAreaElem = getElem('input-area')
function onSubmit(e) {
  e.preventDefault()
  var submitHash = sha256(textAreaElem.value)
  var response = getRandomResponse(submitHash)
  var problem = problemList[selectElem.selectedIndex]
  var correctWord = getCorrectResponse(problem.correct)
  if (problem.hash === submitHash) {
    response = correctWord
  } else {
    while(response === correctWord) response = getRandomResponse()
  }
  alert(problem.name + ": " + response.toUpperCase())
}
submitElem.onclick = onSubmit
