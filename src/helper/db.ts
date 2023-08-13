import { DYNAMO_DB_Table, DB_KEY, dynamoDB } from '@config';
import { AWSError } from 'aws-sdk';
import { DocumentClient } from 'aws-sdk/clients/dynamodb';
import { PromiseResult } from 'aws-sdk/lib/request';

export const getItems = ({
  key,
  columns,
}): Promise<PromiseResult<DocumentClient.QueryOutput, AWSError>> => {
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
