# ES6 Classes - Amateur

## Learning Objectives
By the end of this project, you should be able to:
- Define a Class
- Add methods to a class
- Understand why and how to add a static method to a class
- Extend a class from another
- Understand Metaprogramming and symbols

## Requirements
- Execution environment: Ubuntu 18.04 LTS with NodeJS 12.11.x
- Allowed editors: vi, vim, emacs, Visual Studio Code
- All files must end with a new line.
- Must include a README.md at the root.
- Code should use the `.js` extension.
- Code will be tested using Jest (`npm run test`).
- Linting will be checked using ESLint.
- All tests and linting must pass (`npm run full-test`).

## Setup
1. **Install NodeJS 12.11.x**:  
    ```bash
    curl -sL https://deb.nodesource.com/setup_12.x -o nodesource_setup.sh
    sudo bash nodesource_setup.sh
    sudo apt install nodejs -y
    ```

2. **Verify Installation**:  
    ```bash
    nodejs -v
    npm -v
    ```

3. **Install Jest, Babel, and ESLint**:  
    ```bash
    npm install --save-dev jest
    npm install --save-dev babel-jest @babel/core @babel/preset-env
    npm install --save-dev eslint
    ```

4. **Configuration Files**:
    - `package.json`
    - `babel.config.js`
    - `.eslintrc.js`

    Don't forget to run `npm install` when you have the `package.json`.

## Tasks & File Names

1. **You used to attend a place like this at some point**:  
    *File*: `0-classroom.js`

2. **Let's make some classrooms**:  
    *File*: `1-make_classrooms.js`

3. **A Course, Getters, and Setters**:  
    *File*: `2-hbtn_course.js`

4. **Methods, static methods, computed methods names... MONEY**:  
    *File*: `3-currency.js`

5. **Pricing**:  
    *File*: `4-pricing.js`

6. **A Building**:  
    *File*: `5-building.js`

7. **Inheritance**:  
    *File*: `6-sky_high.js`

8. **Airport**:  
    *File*: `7-airport.js`

9. **Primitive - Holberton Class**:  
    *File*: `8-hbtn_class.js`

10. **Hoisting**:  
    *File*: `9-hoisting.js`
