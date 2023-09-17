class Building {
  constructor(sqft) {
    if (this.constructor === Building) {
      throw new Error('Building is an abstract class and cannot be instantiated directly.');
    }
    if (typeof sqft !== 'number') {
      throw new Error('Sqft must be a number.');
    }
    this._sqft = sqft;
    // Check if the extending class has the method 'evacuationWarningMessage'
    if (this.evacuationWarningMessage === undefined) {
      throw new Error('Class extending Building must override evacuationWarningMessage');
    }
  }

  get sqft() {
    return this._sqft;
  }
}

export default Building;
