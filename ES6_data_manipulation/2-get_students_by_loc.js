export default function getStudentsByLocation(listOfStudents, city) {
  const result = listOfStudents.filter((listOfStudents) => listOfStudents.location === city);
  return result;
}
