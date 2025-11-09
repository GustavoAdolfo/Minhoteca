import type { APIGatewayProxyEventPathParameters, APIGatewayProxyEventQueryStringParameters } from 'aws-lambda';
import type { Logger } from 'winston';

export type UseCaseContextType = {
  body: Record<string, string | string[]> | undefined;
  pathParams: APIGatewayProxyEventPathParameters | undefined;
  query: APIGatewayProxyEventQueryStringParameters | undefined;
  method: string;
  logger: Logger;
};
