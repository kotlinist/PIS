// Функция форматирования строки (из файла)
var rpad = function (str, length) {
  str = str.toString();
  while (str.length < length) str = str + " ";
  return str;
};

// Функция вывода студентов (из файла)
var printStudents = function (students) {
  console.log(
    rpad("Имя", 15),
    rpad("Фамилия", 15),
    rpad("Группа", 8),
    rpad("Оценки", 20)
  );
  for (var i = 0; i <= students.length - 1; i++) {
    console.log(
      rpad(students[i]["name"], 15),
      rpad(students[i]["surname"], 15),
      rpad(students[i]["group"], 8),
      rpad(students[i]["marks"], 20)
    );
  }
  console.log("\n");
};

var groupmates = [
  {
    name: "Александр",
    surname: "Иванов",
    group: "БВТ1702",
    marks: [4, 3, 5],
  },
  {
    name: "Иван",
    surname: "Петров",
    group: "БСТ2201",
    marks: [4, 4, 4],
  },
  {
    name: "Кирилл",
    surname: "Смирнов",
    group: "БАП1801",
    marks: [5, 5, 5],
  },
  {
    name: "Мария",
    surname: "Соколова",
    group: "БВТ1702",
    marks: [5, 4, 5],
  },
  {
    name: "Анна",
    surname: "Федорова",
    group: "БСТ2201",
    marks: [5, 5, 5],
  },
  {
    name: "Дмитрий",
    surname: "Морозов",
    group: "БАП1801",
    marks: [4, 5, 4],
  },
  {
    name: "Елена",
    surname: "Новикова",
    group: "БВТ1702",
    marks: [5, 5, 5],
  },
  {
    name: "Сергей",
    surname: "Козлов",
    group: "БСТ2201",
    marks: [2, 3, 3],
  },
  {
    name: "Ольга",
    surname: "Волкова",
    group: "БАП1801",
    marks: [4, 4, 5],
  },
  {
    name: "Павел",
    surname: "Лебедев",
    group: "БВТ1702",
    marks: [3, 4, 3],
  },
];

// Вывод всех студентов перед запросом ввода
console.log("=== Все студенты ===");
printStudents(groupmates);

// Функция фильтрации студентов по группе
var filterByGroup = function (students, groupName) {
  var filtered = [];
  for (var i = 0; i < students.length; i++) {
    if (students[i]["group"] === groupName) {
      filtered.push(students[i]);
    }
  }
  return filtered;
};

// Функция вычисления средней оценки
var calculateAverage = function (marks) {
  var sum = 0;
  for (var i = 0; i < marks.length; i++) {
    sum += marks[i];
  }
  return sum / marks.length;
};

// Функция фильтрации студентов по средней оценке
var filterByAverageMark = function (students, minAverage) {
  var filtered = [];
  for (var i = 0; i < students.length; i++) {
    var average = calculateAverage(students[i]["marks"]);
    if (average > minAverage) {
      filtered.push(students[i]);
    }
  }
  return filtered;
};

// Запрос группы для фильтрации
var groupInput = prompt("Введите название группы для фильтрации:");
if (groupInput) {
  console.log("=== Студенты группы " + groupInput + " ===");
  var filteredByGroup = filterByGroup(groupmates, groupInput);
  if (filteredByGroup.length > 0) {
    printStudents(filteredByGroup);
  } else {
    console.log("Студенты группы " + groupInput + " не найдены.\n");
  }
}

// Запрос минимальной средней оценки для фильтрации
var averageInput = prompt("Введите минимальный средний балл для фильтрации:");
if (averageInput) {
  var minAverage = parseFloat(averageInput);
  console.log("=== Студенты со средним баллом выше " + minAverage + " ===");
  var filteredByAverage = filterByAverageMark(filteredByGroup, minAverage);
  if (filteredByAverage.length > 0) {
    printStudents(filteredByAverage);
  } else {
    console.log(
      "Студенты со средним баллом выше " + minAverage + " не найдены.\n"
    );
  }
}
