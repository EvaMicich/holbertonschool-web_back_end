// 6-sky_high.js
import Building from './5-building';

class SkyHighBuilding extends Building {
  constructor(sqft, floors) {
    super(sqft); // Passing sqft to the parent class Building's constructor
    this._floors = floors; // Assigning floors to the SkyHighBuilding's attribute
  }

  // Getter for the floors attribute
  get floors() {
    return this._floors;
  }

  // Overriding the evacuationWarningMessage method
  evacuationWarningMessage() {
    return `Evacuate slowly the ${this._floors} floors`;
  }
}

export default SkyHighBuilding;
