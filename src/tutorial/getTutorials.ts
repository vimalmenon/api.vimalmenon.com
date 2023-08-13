import { BaseResponse } from '@common';
import middy from '@middy/core';
import jsonBodyParser from '@middy/http-json-body-parser';
import { APIGatewayEvent } from 'aws-lambda/trigger/api-gateway-proxy';

export const handler = middy(async (event: APIGatewayEvent) => {
  const { code } = event.queryStringParameters ?? {};
  const response = new BaseResponse(code);

  try {
    return response.setData([]).response();
  } catch (error) {
    return response.setMessage(error.message).withError().response();
  }
}).use(jsonBodyParser());
