import { ISocialMedia } from '@types';

import { getItems } from './db';

const columns = ['name', 'url'];

export const getAllSocialMedia = async () => {
  return (await getItems({ key: 'SocialMedia', columns })).Items as ISocialMedia[];
};
