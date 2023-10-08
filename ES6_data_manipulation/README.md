# ES6 Data Manipulation

## 📚 Resources

**Read or Watch**:

- [Array](#)
- [Typed Array](#)
- [Set Data Structure](#)
- [Map Data Structure](#)
- [WeakMap](#)

**Learning Objectives**:

- How to use map, filter, and reduce on arrays
- Understand Typed arrays
- Grasp the Set, Map, and Weak link data structures

## 📝 Requirements

- All files will be executed on Ubuntu 18.04 LTS using NodeJS 12.11.x
- Allowed editors: `vi`, `vim`, `emacs`, `Visual Studio Code`
- All files should end with a newline
- A `README.md` file, at the root of the project directory, is mandatory
- Your code should use the `.js` extension
- Your code will be tested using Jest with the command `npm run test`
- Your code will be verified against lint using ESLint
- Your code needs to pass all the tests and lint. Verify with `npm run full-test`
- All functions must be exported

## 🛠️ Setup

**Install NodeJS 12.11.x**

```bash
curl -sL https://deb.nodesource.com/setup_12.x -o nodesource_setup.sh
sudo bash nodesource_setup.sh
sudo apt install nodejs -y
```

Check installation with:

```bash
$ nodejs -v
v12.11.1

$ npm -v
6.11.3
```

**Install Jest, Babel, and ESLint**

In your project directory:

```bash
npm install --save-dev jest babel-jest @babel/core @babel/preset-env eslint
```

Remember to run `$ npm install` when you have the `package.json`.

## 🚀 Tasks

Detailed instructions for each task can be found in the original provided assignment. Here is a brief list of tasks:

1. **Basic list of objects**: Create a function named `getListStudents`.
2. **More mapping**: Create a function `getListStudentIds`.
3. **Filter**: Create a function `getStudentsByLocation`.
4. **Reduce**: Create a function `getStudentIdsSum`.
5. **Combine**: Create a function `updateStudentGradeByCity`.
6. **Typed Arrays**: Create a function `createInt8TypedArray`.
7. **Set data structure**: Create a function `setFromArray`.
8. **More set data structure**: Create a function `hasValuesFromArray`.
9. **Clean set**: Create a function `cleanSet`.
10. **Map data structure**: Create a function `groceriesList`.
11. **More map data structure**: Create a function `updateUniqueItems`.

## 🌐 Repository

- **GitHub repository**: [holbertonschool-web_back_end](https://github.com/)
- **Directory**: `ES6_data_manipulation`
