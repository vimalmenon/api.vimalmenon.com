const columns = ['name', 'url'];
import { getItems } from './db';

export const getAllSocialMedia = () => {
  return getItems({ key: 'SocialMedia', columns });
};
