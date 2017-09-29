var problemList = [
  {
      label: '1. 100 krát opakovaná lož ...',
      name: 'mh_emo',
      hash: '5fc5bce200956262a6ec0a7b0d86766b6728cfd91ace9b2c8179dc57d670cf1d',
      correct: '259aa8ef98a8b91de574cd904138ef643240c23080cf24da4793a6f10a43fa9d',
  },

  {
      label: '2. Počasie',
      name: 'mh_temperature',
      hash: '425cf60b1051a51738ef7e9ea67bbc4fc7276c1049384a77f57a2832b3def71d',
      correct: '44c5e7071f3a75a22457bc5f06d3e2ba564b4d6ee8165fb0e9087bacf953bcc3',
  },

  {
      label: '3. Koľajnice',
      name: 'mh_sum_over_100',
      hash: '5e343d4f2ee6a9cff164b284c22a82b4fc65b67f2ef1502804754a72f3af7bc2',
      correct: 'd3cec99112255db9bf4963f7798562b6a36f1bd0b2016918629e007d474deb70',
  },

  {
      label: '4. Hviezdičková pyramída',
      name: 'mh_stars',
      hash: '31f46eccca6923dc21e5e8530618df04bb704e0759e7da8ca8f5f010aa7c7db2',
      correct: '486ea46224d1bb4fb680f34f7c9ad96a8f24ec88be73ea8e5a6c65260e9cb8a7',
  },

  {
      label: '5. 3k+1 (Collatz)',
      name: 'et_collatz',
      hash: 'ecc3c1a566a6b52b2cd077b50d1e0b071be46732a0ef1b7307c3334d537d5936',
      correct: 'dea7111a8406e27cfc8bf5f49c5d40898402b0b584b3285f069170a36f9eec31',
  },

  {
      label: '6. Sort',
      name: 'mh_sort',
      hash: 'c52fbfe4a45db3ec8c89834cd3e66ef40599cc13a557bc08d538c80ae812d4f4',
      correct: '60be9861750facbfad8758254a2f76c0cfe78d54459a3bc187d49b1401fcd8e8',
  },

  {
      label: '7. Palindrómy',
      name: 'et_palindrom',
      hash: '69bee726b4ca48d01f842d9e078da166315c1ae1bf54f771c8a76e98de9961b6',
      correct: '3fc4ccfe745870e2c0d99f71f30ff0656c8dedd41cc1d7d3d376b0dbe685e2f3',
  },

  {
      label: '8. Počet deliteľov',
      name: 'et_divisors',
      hash: '02c040b25cda4f35badc567244e44789a74bbbbe1d5ff030e62243e130dddeab',
      correct: 'd34a569ab7aaa54dacd715ae64953455d86b768846cd0085ef4e9e7471489b7b',
  },

  {
      label: '9. Frekvencia písmen v texte',
      name: 'et_letter_freq',
      hash: '95f720c71992354bfbb32731ab6064244a937dd2398fabfad5e440850af67a37',
      correct: 'ab5e9e376f9539179e465f248595caac9789aed486e8da331495e2cf8f4c5634',
  },

  {
      label: '10. Cézarova šifra',
      name: 'et_ceasar',
      hash: 'dae63708d15cfec506ccb1730b8e359d7916bc8d458653c34b91941355bf4e0b',
      correct: '62484e22a6a5ade1ba25cb1b7c55c4b8861de24caddab73c9409742734008b26',
  },

  {
      label: '11. Rímske čísla',
      name: 'mh_roman_numerals',
      hash: 'd92bb51513c12657ecea21dd48813670b18433ec4d324137294b6d360a967d8a',
      correct: 'bbc5e661e106c6dcd8dc6dd186454c2fcba3c710fb4d8e71a60c93eaf077f073',
  },

  {
      label: '12. Štvorce',
      name: 'mh_squares',
      hash: 'f9129fcf0412134d63f6424f74954fa975d92142bbfdb7b20696197ddbce6767',
      correct: 'aa97302150fce811425cd84537028a5afbe37e3f1362ad45a51d467e17afdc9c',
  },

  {
      label: '13. Nsd a nsn',
      name: 'et_gcd_nsn',
      hash: '747faefe510bc966f9958bcb9cf722a472a97f88c72bd6c9b3642f60f0fe18e1',
      correct: '59d6d61431fce7d91388d0c60374ddaadc1acd8370221e11b029621656d5ccec',
  },

  {
      label: '14. Konvertovanie čísla do inej sústavy',
      name: 'et_convert',
      hash: '9506a05d1c465a2e2e054d2a9f7d74224d03d7c819d705eb7434e39d0b5989ce',
      correct: '4cb4ea25583c25647247ae96fc90225d99ad7a6fabc3e2c2fd13c502e323cd9e',
  },

  {
      label: '15. Trojuholníky',
      name: 'mh_trinagles',
      hash: '53b9e8f28ddaaae7fd5e030f5c99fbd36f5bef3955dfb0a57de3465fd47900c3',
      correct: 'a6a2729cbf6bcadce577a31f7f76201d5ce63c57d6c53318000d67714bb354ef',
  },

  {
      label: '16. Počet núl na konci faktoriálu',
      name: 'et_factorial_zero',
      hash: 'f8ace70a0144376b0d7cc63bd297e31ddf2ea3504bbceb0f049dc29a636a7e35',
      correct: '80f189984e5ca70287d13342f6daa0db45cba3c131c4e46dc81360f3a4c4f690',
  },

  {
      label: '17. Púštne ostrovy',
      name: 'mh_islands',
      hash: '2fedef199225813c5001ca71bb1e3604bd9365765690cf5a056f767057bc3109',
      correct: '38a81e87e79631e602bf5fbd307ce2fcd382b1670c585ea09032aac778a80531',
  },

  {
      label: '18. Maxálny súvislý podsúčet',
      name: 'et_max_subsum',
      hash: '5156ffee8a061012f0456403c123b111e880b0090139c14a66e9e76b2c885380',
      correct: 'd70afca615203838da3d858e60dda12f900e83e4a6fb03a63cfadb8576ca8985',
  },

  {
      label: '19. Sudoku solver',
      name: 'et_sudoku',
      hash: '51dd085609c3983d40d5434f73d0be909a49be0a46d020dc1bdbf436ba1269e8',
      correct: '5b7e6bf2dc4a32a6aa4770cd5639c2c7af890fc86c273b5c8567fe5382086bf3',
  },

  {
      label: '20. Počítame',
      name: 'mh_prefix_notation',
      hash: '2aa53a80b5b22cf60bc9f44c4ec2aafea06ac0e1f4561f1c5d50ff7633b22bf1',
      correct: '3a6eb0790f39ac87c94f3856b2dd2c5d110e6811602261a9a923d3bb23adc8b7',
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
  opt.text = problemList[i].label;
  opt.value = problemList[i].name;

  selectElem.add(opt, null);
}

var submitElem = getElem('submit')
var textAreaElem = getElem('input-area')
function onSubmit(e) {
  e.preventDefault()
  var submitHash = sha256(getElem('problem-select').value + textAreaElem.value)
  var response = getRandomResponse(submitHash)
  var problem = problemList[selectElem.selectedIndex]
  var correctWord = getCorrectResponse(problem.correct)
  if (problem.hash === submitHash) {
    response = correctWord
  } else {
    while(response === correctWord) response = getRandomResponse(submitHash)
  }
  alert(problem.name + ": " + response.toUpperCase())
}
submitElem.onclick = onSubmit
