import { DYNAMO_DB_Table, DB_KEY, dynamoDB } from '@config';

export const getItems = ({ key, columns }) => {
  const appKey = `${DB_KEY}#${key}`;
  const params = {
    TableName: DYNAMO_DB_Table ?? '',
    KeyConditionExpression: '#appKey = :appKey',
    ProjectionExpression: columns.join(','),
    ExpressionAttributeNames: {
      '#appKey': 'appKey',
    },
    ExpressionAttributeValues: {
      ':appKey': appKey,
    },
  };
  return dynamoDB.query(params).promise();
};
