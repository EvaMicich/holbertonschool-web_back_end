class Airport {
  constructor(name, code) {
    this._name = name;
    this._code = code;
  }

  // Overriding the default toString method
  toString() {
    return `[object ${this._code}]`;
  }

  // Bonus: Symbol.toPrimitive is a built-in symbol that defines the default conversion of an object into a primitive value.
  // By defining this method, we can control the default string representation even without calling toString method directly.
  [Symbol.toPrimitive](hint) {
    if (hint === 'string') {
      return `[object ${this._code}]`;
    }
    return super[Symbol.toPrimitive](hint);
  }
}
 
export default Airport;
