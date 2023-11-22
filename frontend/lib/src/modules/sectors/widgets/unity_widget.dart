import 'package:flutter/material.dart';

class UnityWidget extends StatelessWidget {
  final bool selected;
  const UnityWidget({Key? key, this.selected = false}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    final colorScheme = Theme.of(context).colorScheme;
    return Container(
      margin: const EdgeInsets.all(8),
      child: Column(
        children: [
          SizedBox(
            width: 150,
            height: 150,
            child: Card(
              color: selected ? colorScheme.primary : colorScheme.secondary,
              child: Icon(
                Icons.apartment_outlined,
                color: colorScheme.onPrimary,
                size: 100,
              ),
            ),
          ),
          const SizedBox(height: 8),
          const Text('Unidade Centro'),
        ],
      ),
    );
  }
}
