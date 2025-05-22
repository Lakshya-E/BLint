// actions.js - your app specific API functions

import { callApi } from "./helper";

export function fetchMenuItems(queryParams) {
  return callApi('get:/menu/items', queryParams);
}

export function addMenuItem(itemData) {
  return callApi('post:/menu/items', itemData);
}

export function updateMenuItem(id, itemData) {
  return callApi(`put:/menu-items/${id}`, itemData);
}

// ... more API functions
