import type { UseCaseContextType } from './useCaseContext.types.ts';

export interface StrategyUseCaseInterface {
  execute(context: UseCaseContextType): Promise<unknown>;
}
