import 'package:flutter/material.dart';

class AppTheme {
  static ThemeData lightTheme() => ThemeData(
        colorScheme: ColorScheme.fromSeed(seedColor: Colors.lightGreen),
        appBarTheme: appBarTheme(),
        useMaterial3: true,
      );

  static AppBarTheme appBarTheme() => const AppBarTheme(
        color: Colors.lightGreen,
        centerTitle: true,
        elevation: 0,
        foregroundColor: Colors.white,
      );
}
