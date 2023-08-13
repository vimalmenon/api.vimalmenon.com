import { getItems } from './db';

export const getTutorials = () => {
  return getItems({ key: 'Tutorial', columns: [] });
};
