import 'package:flutter/material.dart';
import 'package:frontend/src/modules/home/pages/home_page.dart';
import 'package:frontend/src/shared/theme/app_theme.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Responsible sector',
      theme: AppTheme.lightTheme(),
      home: const HomePage(),
    );
  }
}
