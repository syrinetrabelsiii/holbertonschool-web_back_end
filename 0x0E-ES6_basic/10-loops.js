export default function appendToEachArrayValue(array, appendString) {
    const array1 = array;
    for (const value of array) {
      const idx = array.indexOf(value);
      array1[idx] = appendString + value;
    }
  
    return array1;
  }
