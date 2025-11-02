import js from '@eslint/js';
import eslintPluginPrettierRecommended from 'eslint-plugin-prettier/recommended';
import globals from 'globals';
import tseslint from 'typescript-eslint';

export default tseslint.config(
  // Configurações globais
  {
    ignores: ['node_modules', 'dist'],
  },

  // Configuração base do ESLint
  js.configs.recommended,

  // Configurações do TypeScript ESLint
  ...tseslint.configs.recommended,

  // Configuração do Prettier (deve ser a última para sobrescrever outras regras de formatação)
  eslintPluginPrettierRecommended,

  // Suas regras personalizadas
  {
    files: ['**/*.{js,mjs,cjs,ts,mts,cts}'],
    languageOptions: {
      globals: {
        ...globals.node,
      },
    },
    rules: {
      'no-console': 'warn',
      quotes: ['error', 'single'],
      '@typescript-eslint/no-explicit-any': 'warn',
    },
  }
);
