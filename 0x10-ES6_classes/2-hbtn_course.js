class HolbertonCourse {
    constructor(name, length, students) {
      this._name = name;
      this._length = length;
      this._students = Array.isArray(students) ? students : [];
  
      if (typeof name !== 'string') {
        throw new TypeError('Name must be a string');
      }
  
      if (typeof length !== 'number') {
        throw new TypeError('Length must be a number');
      }
  
      if (!Array.isArray(students)) {
        throw new TypeError('Students must be an array');
      }
  
      for (const student of students) {
        if (typeof student !== 'string') {
          throw new TypeError('Each student must be a string');
        }
      }
    }
  
    get name() {
      return this._name;
    }
  
    set name(name) {
      if (typeof name !== 'string') {
        throw new TypeError('Name must be a string');
      }
      this._name = name;
    }
  
    get length() {
      return this._length;
    }
  
    set length(length) {
      if (typeof length !== 'number') {
        throw new TypeError('Length must be a number');
      }
      this._length = length;
    }
  
    get students() {
      return this._students;
    }
  
    set students(students) {
      if (!Array.isArray(students)) {
        throw new TypeError('Students must be an array');
      }
  
      for (const student of students) {
        if (typeof student !== 'string') {
          throw new TypeError('Each student must be a string');
        }
      }
  
      this._students = students;
    }
  }